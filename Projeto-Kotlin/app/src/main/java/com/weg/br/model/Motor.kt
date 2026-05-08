package com.weg.br.model

import androidx.compose.ui.unit.Dp

data class Motor(
    val id: Int,
    val nome: String,
    val x: Dp, // Posição Horizontal
    val y: Dp, // Posição Vertical
    val status: String = "Operando"
)
