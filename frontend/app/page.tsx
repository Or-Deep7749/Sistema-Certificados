"use client"
import { useState } from "react"

interface Certificado {
  nome: string,
  curso: string,
  cargaHoraria: string
}

export default function Home(){
  const [dados, setDados] = useState<Certificado>({
    nome: "",
    curso: "",
    cargaHoraria: ""
  })

  async function gerarCertificado() {
    const resposta = await fetch("http://localhost:5000/certificado",{
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(dados)
    })
    
    if(resposta.ok){
      const arquivo = await resposta.blob()
      const url = window.URL.createObjectURL(arquivo)
      const link = document.createElement("a")
      link.href = url
      link.download = "certificado.pdf"
    }
  }

  return(
    <main className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
      <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md border border-slate-200">
        <h1 className="text-2xl font-bold text-slate-900 text-center mb-6">Sistema - Certificados</h1>
        
        <div className="mb-4">
          <label className="block mb-2 font-semibold text-slate-800 text-sm">Nome</label>
          <input 
            className="w-full border border-slate-300 rounded-lg p-2.5 text-slate-900 bg-white focus:outline-none focus:ring-2 focus:ring-blue-600" 
            value={dados.nome} 
            onChange={(e)=>setDados({...dados, nome: e.target.value})}
          />
        </div>

        <div className="mb-4">
          <label className="block mb-2 font-semibold text-slate-800 text-sm">Curso</label>
          <input 
            className="w-full border border-slate-300 rounded-lg p-2.5 text-slate-900 bg-white focus:outline-none focus:ring-2 focus:ring-blue-600" 
            value={dados.curso} 
            onChange={(e)=>setDados({...dados, curso: e.target.value})}
          />
        </div>

        <div className="mb-6">
          <label className="block mb-2 font-semibold text-slate-800 text-sm">Carga Horária</label>
          <input 
            className="w-full border border-slate-300 rounded-lg p-2.5 text-slate-900 bg-white focus:outline-none focus:ring-2 focus:ring-blue-600" 
            value={dados.cargaHoraria} 
            onChange={(e)=>setDados({...dados, cargaHoraria: e.target.value})}
          />
        </div>

        <button 
          onClick={gerarCertificado} 
          className="w-full bg-blue-600 text-white rounded-lg p-3 hover:bg-blue-700 cursor-pointer font-bold transition duration-200 shadow-md">
          Gerar Certificado
        </button>
      </div>
    </main>
  )
}