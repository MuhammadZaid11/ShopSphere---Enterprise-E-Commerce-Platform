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
        var products = await _productService.GetProductsAsync();

        return View(products);
    }
}