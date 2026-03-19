import React from 'react'

interface ChatMessageProps {
  role: 'user' | 'assistant'
  content: string
  isStreaming?: boolean
}

import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

export const ChatMessage: React.FC<ChatMessageProps> = ({ role, content, isStreaming }) => {
  return (
    <div className={`message ${role} ${isStreaming ? 'streaming' : ''}`}>
      <div className="message-role">{role === 'user' ? 'You' : 'AI'}</div>
      <div className="message-content">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {content}
        </ReactMarkdown>
        {isStreaming && <span className="streaming-dot"></span>}
      </div>
    </div>
  )
}
