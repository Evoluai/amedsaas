import os
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# Configuração de fontes
font_config = FontConfiguration()

# Criar o PDF unificado dos termos LGPD
def create_unified_pdf():
    # Conteúdo HTML unificado
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Documentação LGPD - AmedEvo</title>
        <style>
            @page {
                margin: 2cm;
            }
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }
            h1 {
                color: #0066cc;
                text-align: center;
                border-bottom: 2px solid #0066cc;
                padding-bottom: 10px;
                margin-top: 30px;
            }
            h2 {
                color: #0066cc;
                margin-top: 20px;
                border-bottom: 1px solid #ddd;
                padding-bottom: 5px;
            }
            h3 {
                color: #0066cc;
                margin-top: 15px;
            }
            .cover {
                text-align: center;
                margin: 100px 0;
            }
            .cover h1 {
                font-size: 28px;
                margin-bottom: 20px;
                border: none;
            }
            .cover p {
                font-size: 16px;
                margin: 10px 0;
            }
            .section {
                margin: 30px 0;
                page-break-after: always;
            }
            .footer {
                text-align: center;
                font-size: 0.9em;
                color: #666;
                margin-top: 30px;
                border-top: 1px solid #ddd;
                padding-top: 10px;
            }
            .highlight {
                background-color: #e6f2ff;
                padding: 10px;
                border-radius: 5px;
                margin: 15px 0;
            }
            ol li, ul li {
                margin-bottom: 10px;
            }
            .signature {
                margin-top: 50px;
                border-top: 1px solid #000;
                width: 50%;
                padding-top: 10px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <!-- Capa -->
        <div class="cover">
            <h1>DOCUMENTAÇÃO LGPD</h1>
            <h2>AmedEvo - Sistema de Gestão para Saúde</h2>
            <p>Política de Privacidade | Termos de Uso | Cláusula LGPD</p>
            <p>Versão 1.2 - 27/05/2025</p>
        </div>
        
        <!-- Política de Privacidade -->
        <div class="section">
            <h1>POLÍTICA DE PRIVACIDADE – AMEDEVO</h1>
            
            <p>A AmedEvo respeita sua privacidade. Os dados coletados em nosso sistema são usados exclusivamente para fins operacionais, clínicos, administrativos e legais, conforme a Lei Geral de Proteção de Dados (LGPD – Lei 13.709/2018).</p>
            
            <h2>1. Quais dados coletamos:</h2>
            <ul>
                <li>Informações de empresas e responsáveis (nome, CNPJ, e-mail, telefone).</li>
                <li>Informações de profissionais da saúde (nome, CPF, CRM, contato).</li>
                <li>Informações de pacientes (nome, CPF, dados clínicos, endereço, plano).</li>
                <li>Dados de acesso e navegação (IP, horário de login, ações no sistema).</li>
            </ul>
            
            <h2>2. Finalidades:</h2>
            <ul>
                <li>Garantir o funcionamento e segurança do sistema.</li>
                <li>Permitir o gerenciamento clínico, administrativo e financeiro.</li>
                <li>Cumprir obrigações legais, contratuais e regulatórias.</li>
            </ul>
            
            <h2>3. Seus direitos como titular:</h2>
            <ul>
                <li>Acesso, correção ou exclusão de dados.</li>
                <li>Revogação do consentimento.</li>
                <li>Solicitação de portabilidade e informações sobre uso.</li>
            </ul>
            
            <h2>4. Segurança:</h2>
            <ul>
                <li>Criptografia dos dados sensíveis.</li>
                <li>Controle de acesso por login e perfil.</li>
                <li>Logs e backups automáticos.</li>
            </ul>
            
            <div class="highlight">
                <p><strong>Em caso de dúvidas:</strong> privacidade@amedevo.com.br</p>
                <p><strong>Última atualização:</strong> 27/05/2025</p>
                <p><strong>Versão:</strong> v1.2</p>
            </div>
        </div>
        
        <!-- Termos de Uso -->
        <div class="section">
            <h1>TERMOS DE USO – AMEDEVO</h1>
            
            <p>O sistema AmedEvo é uma plataforma de prontuário eletrônico e gestão em saúde domiciliar. Ao utilizá-lo, você concorda com os seguintes termos:</p>
            
            <ol>
                <li>O acesso ao sistema é individual e intransferível.</li>
                <li>É proibida a inserção de dados falsos ou o uso para fins ilícitos.</li>
                <li>O usuário é responsável pela veracidade dos dados inseridos.</li>
                <li>É obrigatório o cumprimento da LGPD em todas as operações realizadas no sistema.</li>
                <li>A plataforma poderá passar por atualizações que exijam novo aceite.</li>
            </ol>
            
            <h2>CLÁUSULA DE TRATAMENTO DE DADOS PESSOAIS</h2>
            
            <p>A CONTRATADA compromete-se a tratar os dados pessoais e sensíveis armazenados no sistema AmedEvo em conformidade com a Lei nº 13.709/2018 – LGPD, adotando todas as medidas técnicas e administrativas para proteger os dados de acesso não autorizado, vazamentos ou alterações indevidas.</p>
            
            <p>A CONTRATANTE é a controladora dos dados inseridos na plataforma e responsabiliza-se por obter os consentimentos necessários dos titulares, bem como garantir a veracidade e legalidade das informações prestadas.</p>
            
            <p>Em caso de incidente de segurança, ambas as partes deverão comunicar-se imediatamente e colaborar com as autoridades competentes.</p>
            
            <p>Este aceite será renovado sempre que houver atualizações relevantes na política de privacidade ou nos termos do sistema.</p>
            
            <div class="highlight">
                <p><strong>Última atualização:</strong> 27/05/2025</p>
                <p><strong>Versão:</strong> v1.2</p>
            </div>
        </div>
        
        <!-- Termo de Aceite -->
        <div class="section">
            <h1>TERMO DE ACEITE</h1>
            
            <p>Declaro que li e compreendi a Política de Privacidade e os Termos de Uso do sistema AmedEvo, e concordo com todas as condições estabelecidas nos documentos.</p>
            
            <p>Estou ciente de que:</p>
            <ul>
                <li>Meus dados serão tratados conforme a Lei Geral de Proteção de Dados (Lei 13.709/2018).</li>
                <li>Tenho direitos como titular dos dados, incluindo acesso, correção e exclusão.</li>
                <li>Sou responsável pela veracidade das informações fornecidas.</li>
                <li>O sistema poderá ser atualizado, exigindo novo aceite quando necessário.</li>
            </ul>
            
            <p>Este termo representa meu consentimento livre, informado e inequívoco para o tratamento dos meus dados pessoais conforme as finalidades descritas na Política de Privacidade.</p>
            
            <div style="margin-top: 50px;">
                <p>Data: ____/____/________</p>
                
                <div class="signature">
                    <p>Assinatura do Usuário</p>
                </div>
                
                <div class="signature" style="margin-left: 50%;">
                    <p>AmedEvo - Sistema de Gestão para Saúde</p>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>© 2025 AmedEvo - Sistema de Gestão para Saúde. Todos os direitos reservados.</p>
        </div>
    </body>
    </html>
    """
    
    # Salvar o HTML temporário
    temp_html_path = "/home/ubuntu/amedevo_lgpd_package/html/documentacao_lgpd_unificada.html"
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Gerar o PDF
    pdf_path = "/home/ubuntu/amedevo_lgpd_package/pdf/AmedEvo_Documentacao_LGPD.pdf"
    HTML(temp_html_path).write_pdf(pdf_path, font_config=font_config)
    
    return pdf_path

if __name__ == "__main__":
    pdf_path = create_unified_pdf()
    print(f"PDF unificado gerado com sucesso: {pdf_path}")
