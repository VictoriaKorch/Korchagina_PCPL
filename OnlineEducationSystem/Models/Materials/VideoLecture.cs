namespace OnlineEducationSystem.Models.Materials;

public class VideoLecture : LearningMaterial
{
    public int DurationMinutes { get; set; }
    
    public VideoLecture(string title, string videoUrl, int duration) 
        : base(title, videoUrl)
    {
        DurationMinutes = duration;
    }
    
    public override void Display() 
        => Console.WriteLine($"📹 Воспроизведение видео: {Title} ({DurationMinutes} мин)");
    
    public override string GetMaterialType() => "Video";
}