import React, { useState } from 'react';

export const KnowledgeUpload: React.FC = () => {
  const [isUploading, setIsUploading] = useState(false);
  const [lastUpload, setLastUpload] = useState<string | null>(null);

  const handleUpload = () => {
    setIsUploading(true);
    // Simulação de upload
    setTimeout(() => {
      setIsUploading(false);
      setLastUpload('norma_nbr5410.pdf');
    }, 2000);
  };

  return (
    <div className="card mt-8">
      <h3>Base de Conhecimento RAG</h3>
      <p className="text-sm text-white/50 mb-6">Importe PDFs de manuais ou normas técnicas para a memória da IA.</p>
      
      <div className="border-2 border-dashed border-white/10 rounded-xl p-8 flex flex-col items-center justify-center bg-black/20 hover:border-emerald-500/30 transition-all cursor-pointer group">
        <div className="w-12 h-12 rounded-full bg-emerald-500/10 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
           <span className="text-2xl text-emerald-400">↑</span>
        </div>
        <span className="text-sm font-medium">Arraste seu PDF ou clique para selecionar</span>
      </div>

      <button 
        onClick={handleUpload}
        disabled={isUploading}
        className={`mt-6 w-full py-3 ${isUploading ? 'bg-white/10 text-white/30 cursor-not-allowed' : 'bg-emerald-500 hover:bg-emerald-600 text-black'} rounded-lg text-sm font-bold transition-all shadow-lg shadow-emerald-500/10`}
      >
        {isUploading ? 'Processando Documento...' : 'Iniciar Ingestão Semântica'}
      </button>

      {lastUpload && (
        <div className="mt-4 p-3 bg-white/5 rounded-lg border border-emerald-500/20 flex items-center gap-3">
          <div className="w-2 h-2 rounded-full bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.8)]"></div>
          <span className="text-xs font-medium text-white/80">Processado: <strong>{lastUpload}</strong></span>
        </div>
      )}
    </div>
  );
};
