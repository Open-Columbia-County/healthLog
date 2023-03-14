#pragma warning disable CS8618

using Microsoft.EntityFrameworkCore;
namespace healthLog.Models;

public class MyContext : DbContext 
{    
    public MyContext(DbContextOptions options) : base(options) { }    
   
    public DbSet<User> Users { get; set; } 
    // public DbSet<Profile> Profiles {get; set;}
    // public DbSet<SymptomList> SymptomLists {get; set;}
    // public DbSet<MedicationList> MedicationLists {get; set;}
    // public DbSet<Week> Weeks {get; set;}
    // public DbSet<Day> Days {get; set;}
    // public DbSet<Feeling> Feelings {get; set;}
    // public DbSet<Symptom> Symptoms {get; set;}
    // public DbSet<Medication> Medications {get; set;}
    // public DbSet<Sugar> Sugars {get; set;}
    // public DbSet<Food> Foods {get; set;}
    // public DbSet<Sleep> Sleeps {get; set;}
    // public DbSet<SleepTracker> SleepTrackers {get; set;}
    // public DbSet<Provider> Providers {get; set;}
    // public DbSet<Message> Messages {get; set;}
    // public DbSet<Reply> Replys {get; set;}
    // public DbSet<Note> Notes {get; set;}
    // public DbSet<Pdf> Pdfs {get; set;}
}