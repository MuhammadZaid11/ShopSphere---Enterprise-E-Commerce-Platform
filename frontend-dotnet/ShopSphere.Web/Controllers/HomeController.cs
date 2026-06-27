using Microsoft.AspNetCore.Mvc;
using ShopSphere.Web.Services;

namespace ShopSphere.Web.Controllers;

public class HomeController : Controller
{
    private readonly ProductService _productService;

    public HomeController(ProductService productService)
    {
        _productService = productService;
    }

    public async Task<IActionResult> Index()
    {
        try 
        {
            var products = await _productService.GetProductsAsync();
            return View(products);
        }
        catch 
        {
            return View(new List<ShopSphere.Web.Models.Product>());
        }
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ShopSphere.Web.Models.ErrorViewModel { RequestId = System.Diagnostics.Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}