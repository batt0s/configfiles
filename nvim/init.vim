filetype on
filetype indent on
filetype plugin on

set encoding=UTF-8

syntax on
set number
set mouse=a
set mouse=v
set smarttab
set autoindent
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set termguicolors

:nnoremap <C-w><C-w> :w<CR>
:nnoremap <C-w><C-q> :wq<CR>
:nnoremap <C-t><C-t> :terminal<CR>
nnoremap <C-b>n :bn<CR>
nnoremap <C-b>p :bp<CR>
nnoremap <C-b>d :bd<CR>
au filetype go inoremap <C-c> <C-x><C-o>

nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>

inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>

call plug#begin()
Plug 'vim-airline/vim-airline'
Plug 'navarasu/onedark.nvim'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'kyazdani42/nvim-tree.lua'
Plug 'akinsho/bufferline.nvim', { 'tag': 'v2.*' }
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

Plug 'fatih/vim-go', { 'do': ':GoInstallBinaries' }
call plug#end()

let g:onedark_config = { 'style': 'darker' }
colorscheme onedark

lua require 'nvim-tree'.setup {}
nnoremap <C-n> :NvimTreeToggle<CR>

lua require("bufferline").setup{}
