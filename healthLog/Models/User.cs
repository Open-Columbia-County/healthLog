#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace healthLog.Models;

public class User {
    [Key]
    public int UserId {get; set;}
    [Required]
    public string FirstName {get; set;}
    [Required]
    public string LastName {get; set;}
    [Required]
    public string Username {get; set;}
    [Required]
    public string Email {get; set;}
    public int Level {get; set;} = 0;
    [Required]
    public string Password {get; set;}
    [NotMapped]
    [Compare("Password", ErrorMessage ="Passwords don't match")]
    public string Confirm {get; set;}
    public DateTime LoggedOn {get; set;} = DateTime.Now;
    public DateTime CreatedAt { get; set; } = DateTime.Now;
    public DateTime UpdatedAt { get; set; } = DateTime.Now;


    public string FullName() {
        return FirstName + " " + LastName;
    }
}