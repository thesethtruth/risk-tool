/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['example.com'],
  },
  env: {
    CUSTOM_API_URL: process.env.CUSTOM_API_URL,
  },
};

module.exports = nextConfig;
