-- General configs
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.smarttab = true
vim.opt.autoindent = true
vim.opt.expandtab = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.softtabstop = 4
vim.opt.encoding = "utf-8"


-- Keymaps
vim.g.mapleader = " "

function map(mode, shortcut, command)
    vim.api.nvim_set_keymap(mode, shortcut, command, { noremap = true, silent = true })
end

function nmap(shortcut, command)
    map("n", shortcut, command)
end

function imap(shortcut, command)
    map("i", shortcut, command)
end

nmap("<leader>ff", "<cmd>Telescope find_files<cr>")
nmap("<leader>fb", "<cmd>Telescope buffers<cr>")
nmap("<leader>bn", ":bn<CR>")
nmap("<leader>bp", ":bp<CR>")
nmap("<leader>bd", ":bd<CR>")
nmap("<C-n>", ":NvimTreeToggle<CR>")

imap("\"", "\"\"<left>")
imap("'", "''<left>")
imap("(", "()<left>")
imap("{", "{}<left>")
imap("[", "[]<left>")


-- Plugins
require("packer").startup(function() 
    use "wbthomason/packer.nvim"
    use "neovim/nvim-lspconfig"
    use "williamboman/nvim-lsp-installer"
    use "navarasu/onedark.nvim"
    use "kyazdani42/nvim-web-devicons"
    use "kyazdani42/nvim-tree.lua"
    use "nvim-lua/plenary.nvim"
    use "nvim-telescope/telescope.nvim"
    use "vim-airline/vim-airline"
    use "akinsho/bufferline.nvim"
end)

require("nvim-tree").setup {}
require("bufferline").setup {}

-- lsp 
require("nvim-lsp-installer").setup({
    automatic_installation = true,
})
require("lsp_config")
vim.api.nvim_exec("autocmd BufWritePre *.go lua vim.lsp.buf.formatting()", false)
vim.api.nvim_exec("autocmd BufWritePre *.go lua goimports(1000)", false)
imap(".", ".<C-x><C-o>")
vim.api.nvim_exec("set completeopt=menu,menuone,noinsert", false)

-- Colorscheme
require("onedark").setup {
	style = "darker"
}
require("onedark").load()
