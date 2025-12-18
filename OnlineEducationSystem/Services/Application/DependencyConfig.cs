namespace OnlineEducationSystem.Services.Application;

using OnlineEducationSystem.Services.Abstractions;
using OnlineEducationSystem.Services.Implementations;

// Конфигурация зависимостей
public static class DependencyConfig
{
    public static AssignmentService CreateDefaultAssignmentService()
    {
        var emailService = new EmailNotificationService("smtp.gmail.com");
        var localStorage = new LocalStorageService("./assignments");
        var logger = new ConsoleLogger();
        
        return new AssignmentService(emailService, localStorage, logger);
    }
    
    public static CourseService CreateDefaultCourseService()
    {
        var smsService = new SmsNotificationService("api_key_sms_123");
        var logger = new ConsoleLogger();
        
        return new CourseService(smsService, logger);
    }
}