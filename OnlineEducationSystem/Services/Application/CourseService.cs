namespace OnlineEducationSystem.Services.Application;

using OnlineEducationSystem.Models.Users;
using OnlineEducationSystem.Services.Abstractions;

public class CourseService
{
    private readonly NotificationService _notificationService;
    private readonly ILogger _logger;
    
    public CourseService(
        NotificationService notificationService,
        ILogger logger)
    {
        _notificationService = notificationService;
        _logger = logger;
        _logger.Log("CourseService инициализирован");
    }
    
    public void EnrollStudent(Student student, string courseName)
    {
        _logger.Log($"🎓 {student.Name} записан на курс: {courseName}");
        _notificationService.SendNotification(
            student,
            $"Добро пожаловать на курс '{courseName}'! Начало: {DateTime.Now.AddDays(7):yyyy-MM-dd}");
        
        _logger.Log($"Запись на курс завершена для {student.Name}");
    }
}