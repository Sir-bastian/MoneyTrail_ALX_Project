const express = require('express');
const path = require('path');
const app = express();

// Serve static files from the React app
app.use(express.static(path.join(__dirname, 'public')));

// API routes
app.use('/api', (req, res) => {
  // Proxy requests to backend
  const { createProxyMiddleware } = require('http-proxy-middleware');
  createProxyMiddleware({ target: 'http://localhost:5000', changeOrigin: true })(req, res);
});

// Handle other routes by serving index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const port = process.env.PORT || 3003;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
