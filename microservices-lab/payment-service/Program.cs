using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
var app = builder.Build();

// In-memory storage
var payments = new List<Dictionary<string, object>>();
var idCounter = 1;

app.MapGet("/payments", () => payments);

app.MapPost("/payments/process", ([FromBody] Dictionary<string, object> payment) =>
{
    payment["id"] = idCounter++;
    payment["status"] = "SUCCESS";
    payments.Add(payment);
    return Results.Created($"/payments/{payment["id"]}", payment);
});

app.MapGet("/payments/{id}", (int id) =>
{
    var payment = payments.FirstOrDefault(p => (int)p["id"] == id);
    return payment != null ? Results.Ok(payment) : Results.NotFound(new { error = "Payment not found" });
});

app.Run();
