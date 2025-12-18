namespace OnlineEducationSystem.Services.Abstractions;

using OnlineEducationSystem.Models.Materials;

public abstract class StorageService
{
    protected string StorageType { get; set; }
    
    protected StorageService(string storageType = "StorageService")
    {
        StorageType = storageType;
        Console.WriteLine($"Инициализация хранилища: {storageType}");
    }
    
    // Абстрактные методы
    public abstract void SaveMaterial(LearningMaterial material);
    public abstract LearningMaterial GetMaterial(int id);
    public abstract Task SaveMaterialAsync(LearningMaterial material);
    public abstract Task<LearningMaterial> GetMaterialAsync(int id);
    
    // Виртуальный метод с общей логикой
    public virtual void BackupMaterial(LearningMaterial material)
    {
        Console.WriteLine($"[{StorageType}] Резервное копирование: {material.Title}");
    }
}