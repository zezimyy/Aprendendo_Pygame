function love.load()
    --Velocidade inicial do passaro
    bird_Y = 200
    bird_speed = 0
end

function love.draw()
    --Fundo
    love.graphics.setColor(.24, .36, .46)
    love.graphics.rectangle("fill", 0,0,300,388)

    --Passaro
    love.graphics.setColor(.87, .84, .27)
    love.graphics.rectangle("fill", 62, bird_Y, 30, 25)

end

function love.update(dt)
    --Velocidade do passaro aumenta com o tempo
    bird_speed = bird_speed + (516 *dt)
    bird_Y = bird_Y + (bird_speed * dt)
end

function love.keypressed(key)
    --Passaro voar
    if bird_Y > 0 then
        bird_speed = -165
    end
end
