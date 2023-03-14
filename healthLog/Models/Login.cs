#pragma warning disable CS8618
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

[NotMapped]
public class Login
{
    [Required]
    public string LoginUsername {get; set;}
    [Required]
    public string LoginPassword {get; set;}
}