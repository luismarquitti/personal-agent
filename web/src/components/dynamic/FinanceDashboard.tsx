import React, { useEffect, useState } from 'react';
import { Wallet, TrendingUp, TrendingDown, Receipt, ArrowUpRight, ArrowDownRight } from 'lucide-react';

interface Account {
  id: number;
  name: string;
  account_type: string;
  balance: number;
}

interface Transaction {
  id: number;
  description: string;
  amount: number;
  date: string;
  transaction_type: 'income' | 'expense';
}

interface DashboardData {
  total_balance: number;
  accounts: Account[];
  recent_transactions: Transaction[];
}

export const FinanceDashboard: React.FC = () => {
  const [data, setData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/v1/finance/dashboard')
      .then(res => res.json())
      .then(json => {
        setData(json);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching finance dashboard:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="p-8 text-center text-zinc-400">Carregando Painel Financeiro...</div>;
  if (!data) return <div className="p-8 text-center text-red-400">Erro ao carregar dados.</div>;

  return (
    <div className="p-6 bg-zinc-900/50 backdrop-blur-md border border-zinc-800 rounded-2xl shadow-2xl space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-white tracking-tight">Painel Financeiro</h2>
          <p className="text-zinc-400 text-sm">Resumo consolidado das suas contas</p>
        </div>
        <div className="p-3 bg-indigo-500/10 border border-indigo-500/20 rounded-xl">
          <Wallet className="w-6 h-6 text-indigo-400" />
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-4 bg-zinc-800/40 border border-zinc-700/50 rounded-xl">
          <div className="flex items-center gap-2 text-zinc-400 text-xs uppercase tracking-wider mb-2 font-semibold">
            Saldo Total
          </div>
          <div className="text-3xl font-bold text-white tabular-nums">
            R$ {data.total_balance.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
          </div>
        </div>
        <div className="p-4 bg-emerald-500/5 border border-emerald-500/10 rounded-xl">
          <div className="flex items-center gap-2 text-emerald-400 text-xs uppercase tracking-wider mb-2 font-semibold">
            <TrendingUp className="w-3 h-3" /> Receitas
          </div>
          <div className="text-xl font-bold text-emerald-300 tabular-nums">
            R$ 12.450,00 <span className="text-[10px] font-normal text-emerald-500/70 ml-1">ESTIMADO</span>
          </div>
        </div>
        <div className="p-4 bg-rose-500/5 border border-rose-500/10 rounded-xl">
          <div className="flex items-center gap-2 text-rose-400 text-xs uppercase tracking-wider mb-2 font-semibold">
            <TrendingDown className="w-3 h-3" /> Despesas
          </div>
          <div className="text-xl font-bold text-rose-300 tabular-nums">
            R$ 8.920,00 <span className="text-[10px] font-normal text-rose-500/70 ml-1">ESTIMADO</span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Accounts List */}
        <section>
          <div className="flex items-center gap-2 mb-4 text-white font-semibold">
            <Receipt className="w-4 h-4 text-zinc-500" /> 
            Minhas Contas
          </div>
          <div className="space-y-3">
            {data.accounts.map(acc => (
              <div key={acc.id} className="group flex justify-between items-center p-3 rounded-lg border border-transparent hover:border-zinc-800 hover:bg-zinc-800/30 transition-all duration-200">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 bg-zinc-800 rounded-full flex items-center justify-center text-zinc-500 group-hover:bg-zinc-700 transition-colors">
                    {acc.account_type === 'checking' ? 'CH' : 'SV'}
                  </div>
                  <div>
                    <div className="text-zinc-200 font-medium">{acc.name}</div>
                    <div className="text-zinc-500 text-xs capitalize">{acc.account_type}</div>
                  </div>
                </div>
                <div className="text-zinc-200 font-bold tabular-nums">
                  R$ {acc.balance.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Recent Transactions */}
        <section>
          <div className="flex items-center gap-2 mb-4 text-white font-semibold">
            <ArrowUpRight className="w-4 h-4 text-zinc-500" /> 
            Últimas Transações
          </div>
          <div className="space-y-3">
            {data.recent_transactions.map(t => (
              <div key={t.id} className="flex justify-between items-center p-1">
                <div className="flex items-center gap-3">
                  {t.transaction_type === 'income' 
                    ? <ArrowDownRight className="w-4 h-4 text-emerald-500" /> 
                    : <ArrowUpRight className="w-4 h-4 text-rose-500" />}
                  <div>
                    <div className="text-zinc-200 text-sm font-medium">{t.description}</div>
                    <div className="text-zinc-500 text-[10px] uppercase">{new Date(t.date).toLocaleDateString('pt-BR')}</div>
                  </div>
                </div>
                <div className={`text-sm font-bold tabular-nums ${t.transaction_type === 'income' ? 'text-emerald-400' : 'text-zinc-300'}`}>
                  {t.transaction_type === 'income' ? '+' : '-'} R$ {Math.abs(t.amount).toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
                </div>
              </div>
            ))}
            {data.recent_transactions.length === 0 && (
              <div className="text-zinc-600 text-sm italic py-4 text-center">Nenhuma transação encontrada.</div>
            )}
          </div>
        </section>
      </div>
    </div>
  );
};
