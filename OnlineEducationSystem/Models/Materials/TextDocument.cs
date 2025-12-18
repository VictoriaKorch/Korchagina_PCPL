namespace OnlineEducationSystem.Models.Materials;

public class TextDocument : LearningMaterial
{
    public int PageCount { get; set; }
    
    public TextDocument(string title, string content, int pageCount) 
        : base(title, content)
    {
        PageCount = pageCount;
    }
    
    public override void Display() 
        => Console.WriteLine($"📄 Отображение документа: {Title} ({PageCount} страниц)");
    
    public override string GetMaterialType() => "Text";
}