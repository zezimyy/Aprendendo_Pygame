function love.load()
    --Velocidade inicial do passaro
    bird_Y = 200
    bird_speed = 0

    --Area jogavel
    area_jogavel_largura = 300
    area_jogavel_altura = 388
end

function love.draw()
    --Fundo
    love.graphics.setColor(.14, .36, .46)
    love.graphics.rectangle("fill", 0, 0, area_jogavel_largura, area_jogavel_altura)

    --Passaro
    love.graphics.setColor(.87, .84, .27)
    love.graphics.rectangle("fill", 62, bird_Y, 30, 25)

    local pipeWidth = 54
    local pipeSpaceHeight = 100
    local pipeSpaceY = 150

    --tubo
    love.graphics.setColor(.37, .82, .28)
    love.graphics.rectangle("fill", area_jogavel_largura, 0, pipeWidth, pipeSpaceY)
    love.graphics.rectangle("fill", area_jogavel_largura, pipeSpaceY+pipeSpaceHeight, pipeWidth, area_jogavel_altura-pipeSpaceY-pipeSpaceHeight)

    
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
