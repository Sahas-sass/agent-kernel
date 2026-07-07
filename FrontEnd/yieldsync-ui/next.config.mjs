/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://agent-kernel-ir1p.onrender.com/api/:path*',
      },
    ];
  },
};

export default nextConfig;