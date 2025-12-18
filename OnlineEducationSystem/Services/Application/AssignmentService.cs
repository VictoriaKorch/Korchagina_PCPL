namespace OnlineEducationSystem.Services.Application;

using OnlineEducationSystem.Models.Users;
using OnlineEducationSystem.Models.Materials;
using OnlineEducationSystem.Services.Abstractions;

public class AssignmentService
{
    private readonly NotificationService _notificationService;
    private readonly StorageService _storageService;
    private readonly ILogger _logger;
    
    // ВНЕДРЕНИЕ ЗАВИСИМОСТЕЙ ЧЕРЕЗ КОНСТРУКТОР
    public AssignmentService(
        NotificationService notificationService,
        StorageService storageService,
        ILogger logger)
    {
        _notificationService = notificationService ?? 
            throw new ArgumentNullException(nameof(notificationService));
        _storageService = storageService ?? 
            throw new ArgumentNullException(nameof(storageService));
        _logger = logger ?? 
            throw new ArgumentNullException(nameof(logger));
        
        _logger.Log("AssignmentService инициализирован с зависимостями");
    }
    
    public void SubmitAssignment(Student student, LearningMaterial assignment)
    {
        _logger.Log($"📤 Студент {student.Name} отправил задание: {assignment.Title}");
        
        // Сохраняем задание
        _storageService.SaveMaterial(assignment);
        
        // Уведомляем студента
        _notificationService.SendNotification(
            student, 
            $"Ваше задание '{assignment.Title}' отправлено.");
        
        // Уведомляем преподавателя
        var instructor = new Instructor("Доктор Смит", "smith@uni.edu", "Computer Science");
        _notificationService.SendNotification(
            instructor,
            $"Новое задание от {student.Name}: {assignment.Title}");
        
        student.UpdateProgress(5);
        _logger.Log($"📊 Прогресс обновлен: {student.Name} - {student.Progress}%");
    }
    
    public async Task SubmitAssignmentAsync(Student student, LearningMaterial assignment)
    {
        _logger.Log($"⏳ Начата асинхронная отправка для {student.Name}");
        
        await _storageService.SaveMaterialAsync(assignment);
        await _notificationService.SendNotificationAsync(
            student, 
            $"Задание '{assignment.Title}' отправлено (асинхронно).");
        
        student.UpdateProgress(3);
        _logger.Log($"✅ Асинхронная отправка завершена для {student.Name}");
    }
}