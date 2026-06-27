using Microsoft.AspNetCore.Mvc;
using ShopSphere.Web.Services;

namespace ShopSphere.Web.Controllers;

public class ProductController : Controller
{
    private readonly ProductService _productService;

    public ProductController(ProductService productService)
    {
        _productService = productService;
    }

    public async Task<IActionResult> Details(int id)
    {
        var product = await _productService.GetProductAsync(id);

        if (product == null)
            return NotFound();

        return View(product);
    }
}