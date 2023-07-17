local lsp = require("lspconfig")

local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true

local on_attach = function(client, bufnr)
    -- Funcs
    local function buf_set_keymap(...) vim.api.nvim_buf_set_keymap(bufnr, ...) end 
    local function buf_set_option(...) vim.api.nvim_buf_set_option(bufnr, ...) end

    buf_set_option("omnifunc", "v:lua.vim.lsp.omnifunc")

    local opts = { noremap = true , silent = true }
    local function buf_nmap(shortcut, command) buf_set_keymap("n", shortcut, command, opts) end

    -- Mappings
    buf_nmap("gD", "<Cmd>lua vim.lsp.buf.declaration()<CR>")
    buf_nmap("gd", "<Cmd>lua vim.lsp.buf.definition()<CR>")
    buf_nmap("ga", "<Cmd>lua vim.lsp.buf.code_action()<CR>")
    buf_nmap("K", "<Cmd>lua vim.lsp.buf.hover()<CR>")
    buf_nmap("gi", "<Cmd>lua vim.lsp.buf.implementation()<CR>")
    buf_nmap("<C-k>", "<Cmd>lua vim.lsp.buf.signature_help()<CR>")
    buf_nmap("<leader>wa", "<Cmd>lua vim.lsp.buf.add_workspace_folder()<CR>")
    buf_nmap("<leader>wr", "<Cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>")
    buf_nmap("<leader>wl", "<Cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>")
    buf_nmap("<leader>D", "<Cmd>lua vim.lsp.buf.type_definition()<CR>")
    buf_nmap("<leader>rn", "<Cmd>lua vim.lsp.buf.rename()<CR>")
    buf_nmap("gr", "<Cmd>lua vim.lsp.buf.references()<CR>")
    buf_nmap("<leader>e", "<Cmd>lua vim.lsp.diagnostic.show_line_diagnostics()<CR>")
    buf_nmap("<leader>dp", "<Cmd>lua vim.lsp.diagnostic.goto_prev()<CR>")
    buf_nmap("<leader>dn", "<Cmd>lua vim.lsp.diagnostic.goto_next()<CR>")
    buf_nmap("<leader>q", "<Cmd>lua vim.lsp.diagnostic.set_loclist()<CR>")
    buf_nmap("<leader>gf", "<Cmd>lua vim.lsp.buf.formatting()<CR>")



    if client.server_capabilities.document_highlight then
        vim.api.nvim_exec([[
            hi LspReferenceRead cterm=bold ctermbg=DarkMagenta guibg=LightYellow
            hi LspReferenceText cterm=bold ctermbg=DarkMagenta guibg=LightYellow
            hi LspReferenceWrite cterm=bold ctermbg=DarkMagenta guibg=LightYellow
            augroup lsp_document_highlight
                autocmd! * <buffer>
                autocmd CursorHold <buffer> lua vim.lsp.buf.document_highlight()
                autocmd CursorMoved <buffer> lua vim.lsp.buf.clear_references()
            augroup NED
        ]], false)
    end
end


-- Go lsp
lsp.gopls.setup{
    cmd = {"gopls"},
    capabilities = capabilities,
    settings = {
        gopls = {
            experimentalPostfixCompletions = true,
            analyses = {
                unusedparams = true,
                shadow = true,
            },
            staticcheck = true,
        },
    },
    on_attach = on_attach,
}

function goimports(timeoutms)
    local context = { source = { organizeImports = true } }
    vim.validate { context = { context , "t", true } }

    local params = vim.lsp.util.make_range_params()
    params.context = context

    local result = vim.lsp.buf_request_sync(0, "textDocument/codeAction", params, timeout_ms)
    if not result or next(result) == nil then return end
    local actions = result[1].result
    if not actions then return end
    local action = actions[1]

    if action.edit or type(action.command) == "table" then
        if action.edit then
            local client = vim.lsp.get_client_by_id(context.client_id)
            vim.lsp.util.apply_workspace_edit(action.edit, "utf-8")
        end
        if type(action.command) == "table" then
            vim.lsp.buf.execute_command(action.command)
        end
    else
        vim.lsp.buf.execute_command(action)
    end
end

-- C LSP setup
lsp.clangd.setup {
    on_attach = on_attach,
    cmd = {
        "clangd",
        "--background-index",
        "--suggest-missing-includes",
    },
    filetypes = {"c","cpp"},
}

lsp.pylsp.setup {
    on_attach=on_attach,
}

