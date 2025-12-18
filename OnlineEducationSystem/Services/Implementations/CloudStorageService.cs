namespace OnlineEducationSystem.Services.Implementations;

using OnlineEducationSystem.Models.Materials;
using OnlineEducationSystem.Services.Abstractions;

public class CloudStorageService : StorageService
{
    private readonly string _connectionString;
    
    public CloudStorageService(string connectionString) 
        : base("CloudStorageService")
    {
        _connectionString = connectionString;
        Console.WriteLine($"✓ Подключение к облачному хранилищу");
    }
    
    public override void SaveMaterial(LearningMaterial material)
    {
        Console.WriteLine($"💾 Сохранение '{material.Title}' в облако...");
    }
    
    public override LearningMaterial GetMaterial(int id)
    {
        Console.WriteLine($"📥 Получение материала #{id} из облака...");
        return new TextDocument("Документ из облака", "Содержимое из облачного хранилища", 5);
    }
    
    public override async Task SaveMaterialAsync(LearningMaterial material)
    {
        await Task.Delay(200);
        Console.WriteLine($"💾 Асинхронное сохранение '{material.Title}' в облако");
    }
    
    public override async Task<LearningMaterial> GetMaterialAsync(int id)
    {
        await Task.Delay(200);
        Console.WriteLine($"📥 Асинхронное получение материала #{id} из облака");
        return new VideoLecture("Видео из облака", "video_cloud_url", 45);
    }
}