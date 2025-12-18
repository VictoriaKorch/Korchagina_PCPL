namespace OnlineEducationSystem.Services.Implementations;

using OnlineEducationSystem.Models.Materials;
using OnlineEducationSystem.Services.Abstractions;

public class LocalStorageService : StorageService
{
    private readonly string _storagePath;
    
    public LocalStorageService(string storagePath) 
        : base("LocalStorageService")
    {
        _storagePath = storagePath;
        Console.WriteLine($"✓ Локальное хранилище в: {storagePath}");
    }
    
    public override void SaveMaterial(LearningMaterial material)
    {
        Console.WriteLine($"💾 Сохранение '{material.Title}' в {_storagePath}");
    }
    
    public override LearningMaterial GetMaterial(int id)
    {
        Console.WriteLine($"📥 Получение материала #{id} из локального хранилища");
        return new TextDocument("Локальный документ", "Содержимое с диска", 3);
    }
    
    public override async Task SaveMaterialAsync(LearningMaterial material)
    {
        await Task.Delay(100);
        Console.WriteLine($"💾 Асинхронное сохранение '{material.Title}' локально");
    }
    
    public override async Task<LearningMaterial> GetMaterialAsync(int id)
    {
        await Task.Delay(100);
        Console.WriteLine($"📥 Асинхронное получение материала #{id} из локального хранилища");
        return new TextDocument("Асинхронный локальный документ", "Асинхронное содержимое", 4);
    }
    
    public override void BackupMaterial(LearningMaterial material)
    {
        base.BackupMaterial(material);
        Console.WriteLine($"[LocalStorageService] Дополнительное резервное копирование в папку backup/");
    }
}