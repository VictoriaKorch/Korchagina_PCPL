namespace OnlineEducationSystem.Services.Abstractions;

using OnlineEducationSystem.Models.Users;

// Абстрактный класс для службы уведомлений
public abstract class NotificationService
{
    protected string ServiceName { get; set; }
    
    protected NotificationService(string serviceName = "NotificationService")
    {
        ServiceName = serviceName;
        Console.WriteLine($"Инициализация {ServiceName}");
    }
    
    // Абстрактный метод - должен быть реализован в наследниках
    public abstract void SendNotification(User user, string message);
    
    // Абстрактный асинхронный метод
    public abstract Task SendNotificationAsync(User user, string message);
    
    // Виртуальный метод - может быть переопределен
    public virtual string GetServiceInfo()
    {
        return $"Служба: {ServiceName}";
    }
    
    // Общая реализация для всех наследников
    protected void LogNotification(string action)
    {
        Console.WriteLine($"[{ServiceName}] {action} в {DateTime.Now:HH:mm:ss}");
    }
}