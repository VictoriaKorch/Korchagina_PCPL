namespace OnlineEducationSystem.Models.Users;

public class Student : User
{
    public decimal Progress { get; set; }
    
    public Student(string name, string email) : base(name, email)
    {
        Progress = 0;
    }
    
    public override string GetRole() => "Student";
    
    public void UpdateProgress(decimal points)
    {
        Progress = Math.Min(100, Progress + points);
    }
}