namespace OnlineEducationSystem.Services.Abstractions;

// Абстрактный класс логгера (начинается с I по соглашению, но это абстрактный класс)
public abstract class ILogger
{
    protected string LoggerName { get; set; }
    
    protected ILogger(string loggerName = "Logger")
    {
        LoggerName = loggerName;
    }
    
    public abstract void Log(string message);
    public abstract void LogError(string error);
    
    // Виртуальный метод с реализацией по умолчанию
    public virtual void LogWarning(string warning)
    {
        Console.WriteLine($"[{LoggerName} WARNING] {DateTime.Now:HH:mm:ss}: {warning}");
    }
    
    // Общий метод для всех наследников
    protected void LogWithLevel(string level, string message)
    {
        Console.WriteLine($"[{LoggerName} {level}] {DateTime.Now:HH:mm:ss}: {message}");
    }
}