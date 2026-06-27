using ShopSphere.Web.Models;
using System.Text.Json;

namespace ShopSphere.Web.Services;

public class ProductService
{
    private readonly HttpClient _httpClient;

    public ProductService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<List<Product>> GetProductsAsync()
    {
        var response = await _httpClient.GetAsync("/products");

        response.EnsureSuccessStatusCode();

        var json = await response.Content.ReadAsStringAsync();

        return JsonSerializer.Deserialize<List<Product>>(json,
            new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            })!;
    }
}
public async Task<Product?> GetProductAsync(int id)
{
    var response = await _httpClient.GetAsync($"/products/{id}");

    if (!response.IsSuccessStatusCode)
        return null;

    var json = await response.Content.ReadAsStringAsync();

    return JsonSerializer.Deserialize<Product>(
        json,
        new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        });
}