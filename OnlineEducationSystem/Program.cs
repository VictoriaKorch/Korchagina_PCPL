using OnlineEducationSystem.Models.Users;
using OnlineEducationSystem.Models.Materials;
using OnlineEducationSystem.Services.Abstractions;
using OnlineEducationSystem.Services.Implementations;
using OnlineEducationSystem.Services.Application;

Console.WriteLine("=== Online Education System ===");
Console.WriteLine("Dependency Injection с абстрактными классами\n");

// Демонстрация 1: Дефолтные зависимости
Console.WriteLine("\n1. Дефолтные зависимости:");
var defaultService = DependencyConfig.CreateDefaultAssignmentService();
var student1 = new Student("Анна Иванова", "anna@student.edu");
var assignment1 = new TextDocument("Принципы ООП", "Абстракция, инкапсуляция...", 15);

defaultService.SubmitAssignment(student1, assignment1);

// Демонстрация 2: Ручное внедрение зависимостей
Console.WriteLine("\n2. Ручное внедрение зависимостей:");
var smsService = new SmsNotificationService("sms_api_key_789");
var cloudStorage = new CloudStorageService("Server=myServer;Database=myDb;");
var logger = new ConsoleLogger();

var customService = new AssignmentService(smsService, cloudStorage, logger);
var student2 = new Student("Петр Сидоров", "petr@student.edu");
var assignment2 = new VideoLecture("Внедрение зависимостей", "https://video.com/di", 45);

customService.SubmitAssignment(student2, assignment2);

// Демонстрация 3: Асинхронные операции
Console.WriteLine("\n3. Асинхронные операции:");
await customService.SubmitAssignmentAsync(student1, assignment2);

// Демонстрация 4: Сервис курсов
Console.WriteLine("\n4. Сервис курсов:");
var courseService = DependencyConfig.CreateDefaultCourseService();
courseService.EnrollStudent(student1, "Продвинутый C#");

Console.WriteLine("\n✅ Демонстрация завершена!");
Console.WriteLine($"{student1.Name}: Прогресс {student1.Progress}%");
Console.WriteLine($"{student2.Name}: Прогресс {student2.Progress}%");