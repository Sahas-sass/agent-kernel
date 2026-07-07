'use client';

import { useState } from 'react';
import { Send, Sprout, CloudRain } from 'lucide-react';

export default function YieldSyncDashboard() {
  const [messages, setMessages] = useState([
    { role: 'agent', content: 'Ayubowan! I am your YieldSync Agronomy Advisor. How can I help with your farm today?' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = input.trim();
    setInput('');
    setMessages((prev) => [...prev, { role: 'user', content: userMessage }]);
    setIsLoading(true);

    try {
      // Call your Agent Kernel Python Backend!
      const response = await fetch('http://localhost:8000/api/v1/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: userMessage,
          session_id: 'farmer_demo',
          agent: 'agronomy_advisor'
        }),
      });

      const data = await response.json();
      setMessages((prev) => [...prev, { role: 'agent', content: data.result }]);
    } catch (error) {
      setMessages((prev) => [...prev, { role: 'agent', content: 'Connection error. Make sure your Python server is running!' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-[#0a192f] to-slate-900 text-slate-200 font-sans selection:bg-emerald-500/30">
      
      {/* Glassmorphism Navigation Bar */}
      <nav className="fixed top-0 w-full z-50 border-b border-white/10 bg-slate-950/40 backdrop-blur-md">
        <div className="max-w-4xl mx-auto px-4 h-16 flex items-center gap-3">
          <div className="p-2 bg-emerald-500/20 rounded-xl border border-emerald-500/30">
            <Sprout className="w-6 h-6 text-emerald-400" />
          </div>
          <h1 className="text-xl font-medium tracking-wide text-white">YieldSync <span className="text-emerald-400 text-sm opacity-80">Advisor AI</span></h1>
        </div>
      </nav>

      {/* Chat Container */}
      <main className="max-w-4xl mx-auto pt-24 pb-32 px-4 flex flex-col gap-6">
        {messages.map((msg, idx) => (
          <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-[80%] rounded-2xl p-5 shadow-lg ${
              msg.role === 'user' 
                ? 'bg-emerald-600/90 text-white rounded-br-none border border-emerald-500/50' 
                : 'bg-slate-800/60 backdrop-blur-sm text-slate-100 rounded-bl-none border border-white/5'
            }`}>
              <p className="leading-relaxed">{msg.content}</p>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-slate-800/60 backdrop-blur-sm rounded-2xl rounded-bl-none p-5 border border-white/5 flex gap-2 items-center">
              <div className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
              <div className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
              <div className="w-2 h-2 bg-emerald-500 rounded-full animate-bounce"></div>
            </div>
          </div>
        )}
      </main>

      {/* Input Area */}
      <div className="fixed bottom-0 w-full bg-gradient-to-t from-slate-950 via-slate-950/90 to-transparent pb-6 pt-12">
        <form onSubmit={sendMessage} className="max-w-4xl mx-auto px-4">
          <div className="relative flex items-center">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about crop prices, diseases, or weather..."
              className="w-full bg-slate-900/80 backdrop-blur-sm border border-white/10 rounded-2xl py-4 pl-6 pr-14 text-white placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-2xl transition-all"
            />
            <button 
              type="submit"
              disabled={isLoading || !input.trim()}
              className="absolute right-2 p-2 bg-emerald-500 hover:bg-emerald-400 text-slate-900 rounded-xl transition-colors disabled:opacity-50 disabled:hover:bg-emerald-500"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}