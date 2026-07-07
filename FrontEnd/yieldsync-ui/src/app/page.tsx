'use client';

import { useState, useRef, useEffect } from 'react';
import { Send, Sprout, CloudRain, TrendingUp, Bug, AlertCircle } from 'lucide-react';

export default function YieldSyncDashboard() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to the bottom when a new message arrives
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const sendMessage = async (text: string) => {
    if (!text.trim()) return;

    setInput('');
    setMessages((prev) => [...prev, { role: 'user', content: text }]);
    setIsLoading(true);

    try {
      const response = await fetch('/api/v1/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: text,
          session_id: 'farmer_pro',
          agent: 'agronomy_advisor'
        }),
      });

      const data = await response.json();
      
      // NEW: Check if the response was successful (HTTP 200)
      if (response.ok && data.result) {
        setMessages((prev) => [...prev, { role: 'agent', content: data.result }]);
      } else {
        // If it failed, print the exact error the server sent back
        setMessages((prev) => [...prev, { role: 'agent', content: `Server Error: ${JSON.stringify(data)}` }]);
      }

    } catch (error) {
      setMessages((prev) => [
        ...prev, 
        { role: 'agent', content: 'Connection error. Please ensure the YieldSync backend is running.' }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    sendMessage(input);
  };

  // Quick Action Prompts for the empty state
  const quickActions = [
    { icon: <TrendingUp className="w-5 h-5" />, text: "What is the market price for rice?", label: "Market Prices" },
    { icon: <CloudRain className="w-5 h-5" />, text: "What is the weather forecast for Anuradhapura?", label: "Weather" },
    { icon: <Bug className="w-5 h-5" />, text: "My tomato leaves have yellow spots. Help!", label: "Pest Control" },
  ];

  return (
    <div className="flex flex-col h-screen bg-gradient-to-br from-slate-950 via-[#0a192f] to-slate-900 text-slate-200 font-sans selection:bg-emerald-500/30">
      
      {/* Premium Glassmorphism Navbar */}
      <nav className="flex-none z-50 border-b border-white/5 bg-slate-950/60 backdrop-blur-xl shadow-lg">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-gradient-to-br from-emerald-400/20 to-emerald-600/20 rounded-xl border border-emerald-500/30 shadow-[0_0_15px_rgba(16,185,129,0.15)]">
              <Sprout className="w-6 h-6 text-emerald-400" />
            </div>
            <div>
              <h1 className="text-xl font-semibold tracking-tight text-white flex items-center gap-2">
                YieldSync
              </h1>
              <p className="text-xs text-emerald-400/80 font-medium">Agronomy Intelligence AI</p>
            </div>
          </div>
          <div className="hidden sm:flex items-center gap-2 text-xs font-medium text-slate-400 bg-slate-900/50 px-3 py-1.5 rounded-full border border-white/5">
            <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
            System Online
          </div>
        </div>
      </nav>

      {/* Main Chat Area (Scrollable) */}
      <main className="flex-1 overflow-y-auto px-4 sm:px-6 scroll-smooth">
        <div className="max-w-3xl mx-auto py-8 flex flex-col gap-6">
          
          {/* Empty State / Welcome Screen */}
          {messages.length === 0 && (
            <div className="flex flex-col items-center justify-center mt-10 sm:mt-20 animate-in fade-in slide-in-from-bottom-4 duration-700">
              <div className="w-20 h-20 bg-emerald-500/10 rounded-full flex items-center justify-center mb-6 border border-emerald-500/20 shadow-2xl">
                <Sprout className="w-10 h-10 text-emerald-400" />
              </div>
              <h2 className="text-3xl font-bold text-white mb-3 text-center">How can I help your farm today?</h2>
              <p className="text-slate-400 text-center max-w-md mb-10 leading-relaxed">
                I am your AI advisor. I can diagnose crop diseases, track your planting history, check weather, and monitor market prices in Sinhala, Tamil, or English.
              </p>
              
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 w-full">
                {quickActions.map((action, idx) => (
                  <button
                    key={idx}
                    onClick={() => sendMessage(action.text)}
                    className="flex flex-col items-center gap-3 p-5 rounded-2xl bg-slate-800/40 hover:bg-slate-700/50 border border-white/5 hover:border-emerald-500/30 transition-all group text-center"
                  >
                    <div className="text-emerald-400 group-hover:scale-110 transition-transform">
                      {action.icon}
                    </div>
                    <span className="text-sm font-medium text-slate-300">{action.label}</span>
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Chat Messages */}
          {messages.map((msg, idx) => (
            <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in slide-in-from-bottom-2 duration-300`}>
              <div className={`max-w-[90%] sm:max-w-[80%] rounded-3xl p-5 shadow-xl ${
                msg.role === 'user' 
                  ? 'bg-gradient-to-br from-emerald-500 to-emerald-700 text-white rounded-br-sm border border-emerald-400/30' 
                  : 'bg-slate-800/80 backdrop-blur-md text-slate-100 rounded-bl-sm border border-white/10'
              }`}>
                {msg.role === 'agent' && (
                  <div className="flex items-center gap-2 mb-2">
                    <Sprout className="w-4 h-4 text-emerald-400" />
                    <span className="text-xs font-semibold text-emerald-400 uppercase tracking-wider">YieldSync AI</span>
                  </div>
                )}
                <p className="leading-relaxed whitespace-pre-wrap text-[15px]">{msg.content}</p>
              </div>
            </div>
          ))}

          {/* Loading Indicator */}
          {isLoading && (
            <div className="flex justify-start animate-in fade-in">
              <div className="bg-slate-800/80 backdrop-blur-md rounded-3xl rounded-bl-sm p-5 border border-white/10 flex gap-2 items-center shadow-xl">
                <div className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
                <div className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
                <div className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce"></div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </main>

      {/* Modern Input Area */}
      <div className="flex-none p-4 sm:p-6 bg-gradient-to-t from-slate-950 via-slate-950 to-transparent">
        <form onSubmit={handleSubmit} className="max-w-3xl mx-auto relative">
          <div className="relative group">
            <div className="absolute -inset-1 bg-gradient-to-r from-emerald-500/20 to-teal-500/20 rounded-3xl blur opacity-0 group-hover:opacity-100 transition duration-500"></div>
            <div className="relative flex items-center bg-slate-900 border border-white/10 rounded-3xl shadow-2xl overflow-hidden focus-within:border-emerald-500/50 transition-colors">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Message your Agronomy Advisor..."
                className="w-full bg-transparent py-4 pl-6 pr-14 text-slate-100 placeholder:text-slate-500 focus:outline-none text-[15px]"
              />
              <button 
                type="submit"
                disabled={isLoading || !input.trim()}
                className="absolute right-2 p-2.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 rounded-2xl transition-all disabled:opacity-50 disabled:hover:bg-emerald-500 disabled:cursor-not-allowed flex items-center justify-center shadow-lg"
              >
                <Send className="w-5 h-5 ml-0.5" />
              </button>
            </div>
          </div>
          <div className="text-center mt-3">
            <p className="text-[11px] text-slate-500 font-medium">YieldSync AI can make mistakes. Always verify critical pesticide and market data.</p>
          </div>
        </form>
      </div>
    </div>
  );
}