package com.weg.br.ui

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import com.weg.br.R
import com.weg.br.model.Motor

@Composable
fun FactoryScreen() {
    val motores = listOf(
        Motor(1, "Motor W22-01", x = 30.dp, y = 50.dp),
        Motor(2, "Motor W22-02", x = 180.dp, y = 150.dp),
        Motor(3, "Motor W22-03", x = 40.dp, y = 300.dp),
        Motor(4, "Motor W22-04", x = 200.dp, y = 450.dp),
        Motor(5, "Motor W22-05", x = 100.dp, y = 600.dp)
    )

    Box(modifier = Modifier.fillMaxSize()) {
        Image(
            painter = painterResource(id = R.drawable.fabrica),
            contentDescription = "Fundo",
            modifier = Modifier.fillMaxSize(),
            contentScale = ContentScale.FillBounds
        )

        motores.forEach { motor ->
            Image(
                painter = painterResource(id = R.drawable.motor_weg_w22),
                contentDescription = motor.nome,
                modifier = Modifier
                    .size(120.dp)
                    .offset(x = motor.x, y = motor.y)
            )
        }
    }
}