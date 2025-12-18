namespace OnlineEducationSystem.Services.Implementations;

using OnlineEducationSystem.Models.Users;
using OnlineEducationSystem.Services.Abstractions;

public class SmsNotificationService : NotificationService
{
    private readonly string _providerApiKey;
    
    public SmsNotificationService(string providerApiKey) 
        : base("SmsNotificationService")
    {
        _providerApiKey = providerApiKey;
        Console.WriteLine($"✓ SMS служба использует API ключ: {providerApiKey[..5]}...");
    }
    
    public override void SendNotification(User user, string message)
    {
        LogNotification($"Отправка SMS {user.Name}");
        Console.WriteLine($"[SMS для {user.Name}] {message}");
    }
    
    public override async Task SendNotificationAsync(User user, string message)
    {
        await Task.Delay(150);
        LogNotification($"Асинхронная отправка SMS {user.Name}");
        Console.WriteLine($"[ASYNC SMS для {user.Name}] {message}");
    }
}