const primary =  '#8DB700';
const success =  '#5AE043';
const info =  '#008EF4';
const warning =  '#FCDB07';
const danger =  '#FF5016';

export const LIGHT_THEME = {
  name: 'light',
  base: 'default',
  variables: {
    primary,
    success,
    info,
    warning,
    danger,
    charts: {
      primary,
      success,
      info,
      warning,
      danger,
      bg: 'transparent',
      textColor: '#334768',
      axisLineColor: '#a0abb4',
      splitLineColor: '#C0CBD2',
      itemHoverShadowColor: 'rgba(0, 0, 0, 0.5)',
      tooltipBackgroundColor: '#D9E3E8',
      areaOpacity: '0.7',
    },
    bubbleMap: {
      primary,
      success,
      info,
      warning,
      danger,
      titleColor: '#334768',
      areaColor: '#C0CBD2',
      areaHoverColor: '#a0abb4',
      areaBorderColor: '#D9E3E8',
    },
  },
};
