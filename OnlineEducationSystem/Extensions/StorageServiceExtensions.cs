namespace OnlineEducationSystem.Extensions;

using OnlineEducationSystem.Models.Materials;
using OnlineEducationSystem.Services.Abstractions;

// Расширения для StorageService
public static class StorageServiceExtensions
{
    public static async Task<LearningMaterial> GetOrCreateAsync(
        this StorageService storage, 
        int id, 
        Func<LearningMaterial> createFunc)
    {
        try
        {
            var material = await storage.GetMaterialAsync(id);
            return material;
        }
        catch
        {
            var newMaterial = createFunc();
            await storage.SaveMaterialAsync(newMaterial);
            return newMaterial;
        }
    }
}