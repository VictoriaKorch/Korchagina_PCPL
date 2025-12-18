namespace OnlineEducationSystem.Services.Implementations;

using OnlineEducationSystem.Models.Users;
using OnlineEducationSystem.Services.Abstractions;

public class EmailNotificationService : NotificationService
{
    private readonly string _smtpServer;
    
    public EmailNotificationService(string smtpServer) 
        : base("EmailNotificationService")
    {
        _smtpServer = smtpServer;
        Console.WriteLine($"✓ Email служба использует сервер: {smtpServer}");
    }
    
    public override void SendNotification(User user, string message)
    {
        LogNotification($"Отправка email на {user.Email}");
        Console.WriteLine($"[EMAIL на {user.Email}] {message}");
    }
    
    public override async Task SendNotificationAsync(User user, string message)
    {
        await Task.Delay(100);
        LogNotification($"Асинхронная отправка email на {user.Email}");
        Console.WriteLine($"[ASYNC EMAIL на {user.Email}] {message}");
    }
    
    public override string GetServiceInfo()
    {
        return base.GetServiceInfo() + $" (SMTP: {_smtpServer})";
    }
}