import React, { useState } from 'react';

interface Product {
  id?: number;
  name: string;
  brand: string;
  protocol: string;
}

export const HardwareCatalog: React.FC = () => {
  const [products] = useState<Product[]>([
    { id: 1, name: 'Smart Bulb RGB', brand: 'HueLike', protocol: 'Zigbee' },
    { id: 2, name: 'Motion Sensor', brand: 'SafeHome', protocol: 'Z-Wave' },
  ]);

  return (
    <div className="card mt-8">
      <h3>Catálogo de Hardware IoT</h3>
      <div className="overflow-x-auto mt-4">
        <table className="w-full text-left text-sm">
          <thead>
            <tr className="border-b border-white/10 text-white/60">
              <th className="pb-2 font-medium">Nome</th>
              <th className="pb-2 font-medium">Marca</th>
              <th className="pb-2 font-medium">Protocolo</th>
              <th className="pb-2 font-medium">Ações</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/5">
            {products.map((p) => (
              <tr key={p.id} className="hover:bg-white/5 transition-colors">
                <td className="py-3 font-medium">{p.name}</td>
                <td className="py-3 text-white/70">{p.brand}</td>
                <td className="py-3">
                  <span className="px-2 py-0.5 bg-blue-500/20 text-blue-400 rounded-full text-[10px] uppercase font-bold border border-blue-500/30">
                    {p.protocol}
                  </span>
                </td>
                <td className="py-3">
                  <button className="text-emerald-400 hover:text-emerald-300 text-xs font-bold uppercase tracking-wider">Editar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button className="mt-6 w-full py-2 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 rounded-lg text-sm font-bold transition-all">
        + Adicionar Novo Dispositivo
      </button>
    </div>
  );
};
