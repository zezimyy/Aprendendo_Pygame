function love.load()
    --Velocidade inicial do passaro
    bird_Y = 200
    bird_speed = 0

    bird_X = 62
    bird_Width = 30

    --Area jogavel
    area_jogavel_largura = 300
    area_jogavel_altura = 388

    --altura da passagem do tubo
    pipeSpaceHeight = 100
    pipeLargura = 54
    function resetPipe()
        local pipeSpaceMin = 54
        pipeSpaceY = love.math.random(pipeSpaceMin, area_jogavel_altura - pipeSpaceHeight - pipeSpaceMin)
        pipeX = area_jogavel_largura
    end
    resetPipe()
end

function love.draw()
    --Fundo
    love.graphics.setColor(.14, .36, .46)
    love.graphics.rectangle("fill", 0, 0, area_jogavel_largura, area_jogavel_altura)

    --Passaro
    love.graphics.setColor(.87, .84, .27)
    love.graphics.rectangle("fill", bird_X, bird_Y, bird_Width, 25)

    local pipeWidth = 54
    --local pipeSpaceHeight = 100
    --local pipeSpaceY = 150

    --tubo
    love.graphics.setColor(.37, .82, .28)
    love.graphics.rectangle("fill", pipeX, 0, pipeWidth, pipeSpaceY)
    love.graphics.rectangle("fill", pipeX, pipeSpaceY+pipeSpaceHeight, pipeWidth, area_jogavel_altura-pipeSpaceY-pipeSpaceHeight)

    
end

function love.update(dt)
    --Velocidade do passaro aumenta com o tempo
    bird_speed = bird_speed + (516 *dt)
    bird_Y = bird_Y + (bird_speed * dt)

    pipeX = pipeX - (60 * dt)

    if (pipeX + pipeLargura) < 0 then
        resetPipe()
    end

    if 
        bird_X < (pipeX + pipeLargura)
    and 
        (bird_X + bird_Width) > pipeX 
    and 
        bird_Y < pipeSpaceY
    then 
        love.load()
    end
end

function love.keypressed(key)
    --Passaro voar
    if bird_Y > 0 then
        bird_speed = -165
    end
end
