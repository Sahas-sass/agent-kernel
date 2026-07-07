/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        // Whenever the frontend asks for this local URL...
        source: '/api/v1/chat',
        // ...Vercel will secretly forward it to your live Render backend!
        destination: 'https://agent-kernel-ir1p.onrender.com/api/v1/chat',
      },
    ];
  },
};

export default nextConfig;