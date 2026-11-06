describe('The Primer v2 — Parite ve Regresyon E2E Test Süiti', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000');
  });

  it('(a) Diferansiyel Parite Testi — İstemci ONNX çıkarım olasılığı Oracle ile uyuşmalı', () => {
    cy.fixture('../../tests/parite.json').then((testCases) => {
      testCases.forEach((testCase) => {
        cy.window().then((win) => {
          const clientProb = win.predictONNX(testCase.girdiler);
          const oracleProb = testCase.oracle_olasilik;
          const diff = Math.abs(clientProb - oracleProb);
          expect(diff).to.be.lessThan(1e-4);
        });
      });
    });
  });

  it('(b) Regresyon Testi — Yeni model devreye girdiğinde 20+ adım kırılmadan tamamlanmalı', () => {
    cy.get('[data-cy="start-btn"]').click();
    
    for (let step = 1; step <= 21; step++) {
      cy.get('[data-cy="scene-title"]').should('be.visible');
      cy.get('[data-cy="option-btn-0"]').click();
      cy.get('[data-cy="next-btn"]').click();
    }
    
    cy.get('[data-cy="game-completed"]').should('contain', 'Tebrikler');
  });
});
