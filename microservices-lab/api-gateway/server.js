const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Proxy routes
app.use('/items', createProxyMiddleware({
    target: 'http://item-service:8081',
    changeOrigin: true
}));

app.use('/orders', createProxyMiddleware({
    target: 'http://order-service:8082',
    changeOrigin: true
}));

app.use('/payments', createProxyMiddleware({
    target: 'http://payment-service:8083',
    changeOrigin: true
}));

// Health check
app.get('/', (req, res) => {
    res.json({ message: 'API Gateway is running', status: 'OK' });
});

const PORT = 8080;
app.listen(PORT, () => {
    console.log(`API Gateway running on port ${PORT}`);
});
