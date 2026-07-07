/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        // The wildcard :path* catches everything after /api/
        source: '/api/:path*',
        // And perfectly mirrors it to your Render backend
        destination: 'https://agent-kernel-ir1p.onrender.com/api/:path*',
      },
    ];
  },
};

export default nextConfig;