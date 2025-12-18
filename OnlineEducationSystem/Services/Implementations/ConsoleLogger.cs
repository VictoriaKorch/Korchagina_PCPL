namespace OnlineEducationSystem.Services.Implementations;

using OnlineEducationSystem.Services.Abstractions;

public class ConsoleLogger : ILogger
{
    public ConsoleLogger() : base("ConsoleLogger")
    {
        Console.WriteLine($"✓ Инициализация консольного логгера");
    }
    
    public override void Log(string message)
    {
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine($"[LOG] {DateTime.Now:HH:mm:ss}: {message}");
        Console.ResetColor();
    }
    
    public override void LogError(string error)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine($"[ERROR] {DateTime.Now:HH:mm:ss}: {error}");
        Console.ResetColor();
    }
}