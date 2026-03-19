import { MainLayout } from './components/layout/MainLayout'
import { Omnibar } from './components/layout/Omnibar'
import { SystemDashboard } from './components/dashboard/SystemDashboard'
import { ChatMessage } from './components/dashboard/ChatMessage'
import { useChatStore } from './store/useChatStore'
import { useSocket } from './lib/useSocket'

function App() {
  const { messages } = useChatStore()
  const { sendMessage } = useSocket()

  const handleSend = (message: string) => {
    sendMessage(message)
  }

  return (
    <MainLayout>
      <div className="dashboard">
        <header className="dashboard-header">
          <h1>Command Center</h1>
          <p className="subtitle">
            Welcome to the Personal AI Core. Select a module from the sidebar to get started.
          </p>
        </header>
        
        <SystemDashboard />

        <section className="chat-history mt-12 mb-8 flex-1">
          <h3 className="mb-4 text-slate-400 uppercase text-xs font-bold tracking-widest">Interaction Log</h3>
          <div className="space-y-4">
            {messages.length === 0 && (
              <p className="text-slate-400 italic text-sm">No recent interactions.</p>
            )}
            {messages.map((msg) => (
              <ChatMessage 
                key={msg.id} 
                role={msg.role} 
                content={msg.content} 
                isStreaming={msg.isStreaming} 
              />
            ))}
          </div>
        </section>

        <Omnibar onSend={handleSend} />
      </div>
    </MainLayout>
  )
}

export default App
