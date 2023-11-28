export const timeStep = 30;

export const specialHours =  {
    1: {
        from: 12.50 * 60,
        to: 16 * 60,
        class: 'closed',
        label: 'Cerrado'
    },
    2: {
        from: 13 * 60,
        to: 16 * 60,
        class: 'closed',
        label: 'Cerrado'
    },
    3: {
        from: 13 * 60,
        to: 16 * 60,
        class: 'closed',
        label: 'Cerrado'
    },
    4: {
        from: 13 * 60,
        to: 16 * 60,
        class: 'closed',
        label: 'Cerrado'
    },
    5: {
        from: 13 * 60,
        to: 16 * 60,
        class: 'closed',
        label: 'Cerrado'
    },
    6: {
        from: 13 * 60,
        to: 20 * 60,
        class: 'closed',
        label: 'Cerrado'
    },
    7: {
      from: 7 * 60,
      to: 20 * 60,
      class: 'closed',
      label: 'Cerrado'
    }
  }


export const events = [
    {
        start: '2023-11-28 10:00',
        end: '2023-11-28 11:00',
        title: 'Libre',
        content: 'Click para reservar',
        class: 'free',
        free: true
    },
    {
        start: '2023-11-28 18:00',
        end: '2023-11-28 19:00',
        title: 'Ocupado',
        class: 'ocupado',
        free: true
    }
]