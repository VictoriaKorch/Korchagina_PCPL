namespace OnlineEducationSystem.Models.Users;

public class Instructor : User
{
    public string Specialization { get; set; }
    
    public Instructor(string name, string email, string specialization) 
        : base(name, email)
    {
        Specialization = specialization;
    }
    
    public override string GetRole() => "Instructor";
}