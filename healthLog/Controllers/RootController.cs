using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using healthLog.Models;
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;

namespace healthLog.Controllers;

public class RootController : Controller
{
    private readonly ILogger<RootController> _logger;

    private MyContext db;  // or use _context instead of db

    public RootController(ILogger<RootController> logger, MyContext context)
    {
        _logger = logger;
        db = context; // if you use _context above use it here too
    }

    private int? uid {
        get {
            return HttpContext.Session.GetInt32("uid");
        }
    }
    private int? level {
        get {
            return HttpContext.Session.GetInt32("level");
        }
    }
    private string? fullName {
        get {
            return HttpContext.Session.GetString("fullName");
        }
    }
    private string? username {
        get {
            return HttpContext.Session.GetString("username");
        }
    }
    private string? first {
        get {
            return HttpContext.Session.GetString("first");
        }
    }

    [HttpGet("")]
    public IActionResult Index()
    {
        if(uid != null) {
            return RedirectToAction("Dashboard");
        }
        else {
            return View("Index");
        }
    }

    [HttpGet("/About")]
    public IActionResult About()
    {
        return View("About");  
    }
    
    [HttpGet("/Contact")]
    public IActionResult Contact()
    {
        return View("Contact");  
    }

    [HttpGet("/LogReg")]
    public IActionResult LogReg()
    {
        if(uid != null) {
            return RedirectToAction("Dashboard");
        }
        else {
            return View("LogReg");
        }
    }

    [HttpPost("/Login")]
    public IActionResult Login(Login getUser)
    {
        if(!ModelState.IsValid) {
            return View("LogReg");
        }
        else {
            User? userInDb = db.Users.FirstOrDefault(u => u.Username == getUser.LoginUsername);
            if(userInDb == null) {
                ModelState.AddModelError("LoginUsername", "Invalid Username");
                return View("LogReg");
            }
            else {
                PasswordHasher<Login> hash = new PasswordHasher<Login>();
                var result = hash.VerifyHashedPassword(getUser, userInDb.Password, getUser.LoginPassword);
                if(result == 0) {
                    ModelState.AddModelError("LoginPassword", "Invalid Password");
                    return View("LogReg");
                }
                else {
                    userInDb.LoggedOn = DateTime.Now;
                    db.Users.Update(userInDb);
                    db.SaveChanges();
                    HttpContext.Session.SetString("fullName", userInDb.FullName());
                    HttpContext.Session.SetString("first", userInDb.FirstName);
                    HttpContext.Session.SetString("username", userInDb.Username);
                    HttpContext.Session.SetInt32("uid", userInDb.UserId);
                    HttpContext.Session.SetInt32("level", userInDb.Level);
                    return RedirectToAction("Dashboard");
                }
            }
        }
    }

    [HttpPost("/Reg")]
    public IActionResult Reg(User newUser)
    {
        if(!ModelState.IsValid) {
            return View("LogReg");
        }
        else {
            PasswordHasher<User> hash = new PasswordHasher<User>();
            newUser.Password = hash.HashPassword(newUser, newUser.Password);
            db.Users.Add(newUser);
            db.SaveChanges();
            if(newUser.UserId == 1) {
                newUser.Level = 24;
                db.Users.Update(newUser);
                db.SaveChanges();
            }
            HttpContext.Session.SetString("fullName", newUser.FullName());
            HttpContext.Session.SetString("first", newUser.FirstName);
            HttpContext.Session.SetString("username", newUser.Username);
            HttpContext.Session.SetInt32("uid", newUser.UserId);
            HttpContext.Session.SetInt32("level", newUser.Level);
            return RedirectToAction("Dashboard");
        }
    }

    [HttpGet("/Logout")]
    public IActionResult Logout()
    {
        HttpContext.Session.Clear();
        return RedirectToAction("Index");
    }

    [HttpGet("/Dashboard")]
    public IActionResult Dashboard()
    {
        User? theUser = db.Users.FirstOrDefault(u => uid == u.UserId);
        if(theUser.CreatedAt == theUser.LoggedOn) {
            ViewBag.Welcome = "Welcome New User";
        }
        else if(theUser.CreatedAt != theUser.LoggedOn) {
            ViewBag.Welcome = "Welcome back!";
        }
        return View("Dashboard");  
    }


    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
public class SessionCheckAttribute : ActionFilterAttribute
{
    public override void OnActionExecuting(ActionExecutingContext context)
    {
        int? uid = context.HttpContext.Session.GetInt32("uid");
        if(uid == null)
        {
            context.Result = new RedirectToActionResult("Index", "Root", null);
        }
    }
}
public class AdminCheckAttribute : ActionFilterAttribute
{
    public override void OnActionExecuting(ActionExecutingContext context)
    {
        int? level = context.HttpContext.Session.GetInt32("level");
        if(level != 24)
        {
            context.Result = new RedirectToActionResult("Index", "Root", 24);
        }
    }
}