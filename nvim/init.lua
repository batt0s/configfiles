-- General configs
require("set")

-- Keymaps
require("keymaps")

-- Plugins
require("plugins")

-- lsp and autocompletion
require("lsp_config")
require("luasnip.loaders.from_vscode").lazy_load()
vim.api.nvim_exec("autocmd BufWritePre *.go lua vim.lsp.buf.formatting()", false)
vim.api.nvim_exec("autocmd BufWritePre *.go lua goimports(1000)", false)
vim.opt.completeopt = { "menu" , "menuone" , "noinsert" }
require("cmp_config")

