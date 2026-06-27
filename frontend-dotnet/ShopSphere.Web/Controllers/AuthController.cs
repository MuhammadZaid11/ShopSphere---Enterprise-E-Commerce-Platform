using Microsoft.AspNetCore.Mvc;

namespace ShopSphere.Web.Controllers;

public class AuthController : Controller
{
    [HttpGet]
    public IActionResult Login()
    {
        return View();
    }

    [HttpPost]
    public IActionResult Login(string email, string password)
    {
        // In a real app, this would call the FastAPI backend to get a JWT token
        // and set it in a cookie or session.
        return RedirectToAction("Index", "Home");
    }

    [HttpGet]
    public IActionResult Register()
    {
        return View();
    }

    [HttpPost]
    public IActionResult Register(string email, string password)
    {
        // Call FastAPI to register user
        return RedirectToAction("Login");
    }
}
