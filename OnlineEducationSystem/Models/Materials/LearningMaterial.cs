namespace OnlineEducationSystem.Models.Materials;

public abstract class LearningMaterial
{
    public int Id { get; set; }
    public string Title { get; set; }
    public string Content { get; set; }
    
    public LearningMaterial(string title, string content)
    {
        Title = title;
        Content = content;
    }
    
    public abstract void Display();
    public abstract string GetMaterialType();
}